import { Component, OnInit, Input  } from '@angular/core';
import { RecipesService } from '../shared/services/recipes.service';
import { Recipe } from '../shared/models/recipe';

@Component({
  selector: 'app-recipe-details',
  templateUrl: './recipe-details.component.html',
  styleUrls: ['./recipe-details.component.css']
})

export class RecipeDetailsComponent implements OnInit {

  //@Input() recipe : Recipe = new Recipe ("","","");

  recipe: Recipe = new Recipe("","","");

  constructor(private recipeService: RecipesService) {}

  ngOnInit() {
    // Subscribe to changes in the selected recipe
    this.recipeService.getSelectedRecipe().subscribe((recipe: Recipe | null) => {
      if (recipe) {
        // Handle the case when recipe is not null
        this.recipe = recipe;
      } else {
        // Handle the case when recipe is null
        this.recipe = new Recipe('', '', '');  // or any default handling
      }
    });
  }
  
}
