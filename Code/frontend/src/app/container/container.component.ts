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
  selectedRecipe: Recipe = new Recipe('', '', '');
  addRecipeMode: boolean = false;
  selectMode: boolean = false;
  newRecipe: Recipe = new Recipe('', '', '');
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
    // Activate add recipe mode
    this.addRecipeMode = true;
    // Reset new recipe form
    this.newRecipe = new Recipe('', '', '');
  }

  onSubmit() {
    // Add the new recipe to the 
    if (this.user_id!=null) {
      this.recipesService.addRecipe(this.newRecipe, this.user_id).subscribe((recipe: Recipe) => {
        this.recipes.push(recipe); // Add to local list after successful API response
        this.addRecipeMode = false; // Exit add mode
      });
    }
  }

  cancelCreation() {
    // Deactivate add recipe mode without saving
    this.addRecipeMode = false;
  }

  ngOnDestroy() {
    // Clean up subscriptions
    if (this.recipeSubscription) {
      this.recipeSubscription.unsubscribe();
    }
  }
}
