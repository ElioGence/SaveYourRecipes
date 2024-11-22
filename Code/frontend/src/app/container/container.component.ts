import { Component, OnInit, OnDestroy } from '@angular/core';
import { Recipe } from '../shared/models/recipe';
import { RecipesService } from '../shared/services/recipes.service';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-container',
  templateUrl: './container.component.html',
  styleUrls: ['./container.component.css']
})
export class ContainerComponent implements OnInit, OnDestroy {
  recipes: Recipe[] = [];
  selectedRecipe: Recipe = new Recipe(0,0,'', '', '');
  addRecipeMode: boolean = false;
  modifyRecipeMode: boolean = false;
  selectMode: boolean = false;
  newRecipe: Recipe = new Recipe(0,0,'', '', '');
  private recipeSubscription: Subscription | null = null;
  user_id: string | null = null;

  constructor(private recipesService: RecipesService, private router: Router) {}

  ngOnInit() {
    // Retrieve user ID from localStorage
    this.user_id = localStorage.getItem('user_id');
    if (this.user_id===null) {
      // If user_id is not found, redirect to login page
      this.router.navigate(['/login']);
      return;
    }

    // Fetch recipes from the API using the user_id
    this.recipesService.getRecipes(this.user_id).subscribe((recipes: Recipe[]) => {
      this.recipes = recipes;
    });

    // Subscribe to selected recipe changes
    this.recipeSubscription = this.recipesService.getSelectedRecipe().subscribe((recipe: Recipe | null) => {
      if (recipe) {
        this.selectedRecipe = recipe;
        this.selectMode = true;
      }
    });
  }

  onRecipeSelected(recipe: Recipe) {
    // Update selected recipe via service
    this.recipesService.setSelectedRecipe(recipe);
    this.selectMode = true;
  }

  onAddRecipe() {
    this.addRecipeMode = true;
    this.modifyRecipeMode = false;
    this.newRecipe = new Recipe(0,0,'', '', '');
  }

  onDeleteRecipe() {
    this.modifyRecipeMode = false;
    this.addRecipeMode = false;
    if (this.selectedRecipe.id !== 0 && this.user_id) {
      this.recipesService.deleteRecipe(this.selectedRecipe.id).subscribe(() => {
        this.recipes = this.recipes.filter(recipe => recipe.id !== this.selectedRecipe.id);
        this.selectedRecipe = new Recipe(0, 0, '', '', ''); 
        this.selectMode = false; 
      });
    }
  }
  

  onModifyRecipe() {
    this.modifyRecipeMode = true;
    this.addRecipeMode=false;
  }

  onSubmit() {
    if (this.addRecipeMode){
      if (this.user_id!=null) {
        this.recipesService.addRecipe(this.newRecipe, this.user_id).subscribe((recipe: Recipe) => {
          this.recipes.push(recipe); 
          this.addRecipeMode = false; 
        });
      }
    } else if (this.modifyRecipeMode) {
      if (this.user_id) {
        this.recipesService.modifyRecipe(this.selectedRecipe.id, this.newRecipe).subscribe((updatedRecipe: Recipe) => {
          const index = this.recipes.findIndex(recipe => recipe.id === this.selectedRecipe.id);
          if (index !== -1) {
            this.recipes[index] = updatedRecipe; 
          }
          this.modifyRecipeMode = false;
          this.recipesService.setSelectedRecipe(this.newRecipe);
        });
      }
    }
  }

  cancel() {
    this.modifyRecipeMode = false; 
    this.addRecipeMode = false;
  }

  ngOnDestroy() {
    if (this.recipeSubscription) {
      this.recipeSubscription.unsubscribe();
    }
  }
}
