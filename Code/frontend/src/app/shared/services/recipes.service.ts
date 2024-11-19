import { Injectable } from '@angular/core';
import { Recipe } from '../models/recipe';
import { Ingredient } from '../models/ingredients';
import { BehaviorSubject,Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RecipesService {

    private recipes: Recipe[] = [
        new Recipe("Gnocchi Chèvre-Epinard","Délicieux plat végétarien, 50cl Crème + 1 chèvre","https://www.marmiton.org/recettes/recette_gnocchi-aux-epinards-et-chevre_222929.aspx")
    ];

    private recipesSubject: BehaviorSubject<Recipe[]> = new BehaviorSubject<Recipe[]>([]);
    private selectedRecipeSubject: BehaviorSubject<Recipe> = new BehaviorSubject(new Recipe("","",""));

    getRecipes(): Recipe[] {
        return this.recipes;
    }

    getSelectedRecipe(): Observable<Recipe> {
        return this.selectedRecipeSubject.asObservable();
    }

    setSelectedRecipe(recipe: Recipe): void {
        this.selectedRecipeSubject.next(recipe);
    }
}