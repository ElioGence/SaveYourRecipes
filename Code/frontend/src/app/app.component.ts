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
    // Remove user_id from localStorage
    localStorage.removeItem('user_id');

    // Reset recipes array
    this.recipes = [];

    // Optionally, you can reset the selected recipe in the service
    this.recipesService.setSelectedRecipe(new Recipe("","",""));

    // Navigate to the login or home page if needed
    this.router.navigate(['/login']);

    this.recipesService.setSelectedRecipe(new Recipe("","",""))
  }
}
