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
  
  selectedRecipe: Recipe = new Recipe("","","");

  constructor(private recipesService: RecipesService) { }

  onRecipeClick(recipe: Recipe) {
    this.recipeSelected.emit(recipe);
    this.selectedRecipe = recipe;
  }

  isSelected(recipe: Recipe) {
    return this.selectedRecipe && this.selectedRecipe.name === recipe.name;
  }

  onAddRecipeClick() {
    this.addRecipe.emit();
  }
}