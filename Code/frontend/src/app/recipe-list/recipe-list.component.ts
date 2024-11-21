import { Component, Input, EventEmitter, Output } from '@angular/core';
import { Recipe } from '../shared/models/recipe';
import { RecipesService } from '../shared/services/recipes.service';

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})

export class RecipeListComponent {
  
  @Input() recipes: Recipe[] = [];
  @Output() recipeSelected: EventEmitter<Recipe> = new EventEmitter<Recipe>();
  @Output() addRecipe: EventEmitter<void> = new EventEmitter<void>(); 
  @Output() deleteRecipe: EventEmitter<Recipe> = new EventEmitter<Recipe>();
  @Output() modifyRecipe: EventEmitter<Recipe> = new EventEmitter<Recipe>();
  
  selectedRecipe: Recipe = new Recipe(0,0,"","","");

  constructor(private recipesService: RecipesService) { }

  onRecipeClick(recipe: Recipe) {
    this.recipeSelected.emit(recipe);
    this.selectedRecipe = recipe;
  }

  isSelected(recipe: Recipe) {
    return this.selectedRecipe && this.selectedRecipe.id === recipe.id;
  }

  onAddRecipeClick() {
    this.addRecipe.emit();
  }

  onDeleteRecipeClick() {
    this.deleteRecipe.emit(this.selectedRecipe);
  }
  
  onModifyRecipeClick() {
    this.modifyRecipe.emit(this.selectedRecipe);
  }
  
}