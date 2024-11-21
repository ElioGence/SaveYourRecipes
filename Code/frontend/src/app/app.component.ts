import { Component } from '@angular/core';
import { Recipe } from './shared/models/recipe';
import { Router } from '@angular/router';
import { RecipesService } from './shared/services/recipes.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  recipes: Recipe[] = [];

  title = 'SaveYourRecipes';

  constructor(private router: Router, private recipesService: RecipesService) {}

  resetApp(): void {
    localStorage.removeItem('user_id');

    this.recipes = [];

    this.recipesService.setSelectedRecipe(new Recipe(0,0,"","",""));

    this.router.navigate(['/login']);

    this.recipesService.setSelectedRecipe(new Recipe(0,0,"","",""))
  }

  resetAppSignUp(): void {
    localStorage.removeItem('user_id');

    this.recipes = [];

    this.recipesService.setSelectedRecipe(new Recipe(0,0,"","",""));

    this.recipesService.setSelectedRecipe(new Recipe(0,0,"","",""))
  }
}
