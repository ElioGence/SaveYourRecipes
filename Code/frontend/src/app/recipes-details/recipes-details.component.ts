import { Component, OnInit  } from '@angular/core';
import { Recipe } from '../shared/models/recipe';
import { RecipesService } from '../shared/services/recipes.service';

@Component({
  selector: 'app-pizza-details',
  templateUrl: './pizza-details.component.html',
  styleUrls: ['./pizza-details.component.css']
})

export class RecipesDetailsComponent implements OnInit {

  //@Input() recipe : Recipe = new Recipe ("","","");

  recipe: Recipe = new Recipe( );

  constructor(private recipeService: RecipesService) {}

  ngOnInit() {
    // Souscrire aux changements de la pizza sélectionnée
    this.recipeService.getSelectedRecipe().subscribe((recipe: Recipe) => {
      this.recipe = recipe;
    });
  }
  
}
