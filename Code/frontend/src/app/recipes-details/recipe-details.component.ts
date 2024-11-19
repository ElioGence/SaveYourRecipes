import { Component, OnInit  } from '@angular/core';
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
    // Souscrire aux changements de la pizza sélectionnée
    this.recipeService.getSelectedRecipe().subscribe((recipe: Recipe) => {
      this.recipe = recipe;
    });
  }
  
}
