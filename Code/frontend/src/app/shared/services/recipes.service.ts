import { Injectable } from '@angular/core';
import { Recipe } from '../models/recipe';
import { Ingredient } from '../models/ingredients';
import { BehaviorSubject,Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RecipesService {

    private recipes: Recipe[] = [
    
    ];

    private recipesSubject: BehaviorSubject<Recipe[]> = new BehaviorSubject<Pizza[]>([]);
    private selectedRecipeSubject: BehaviorSubject<Recipe> = new BehaviorSubject(new Pizza("","void.png",""));

    getRecipes(): Recipe[] {
        return this.recipes;
    }

    getSelectedPizza(): Observable<Recipe> {
        return this.selectedRecipeSubject.asObservable();
    }

    setSelectedPizza(recipe: Recipe): void {
        this.selectedRecipeSubject.next(recipe);
    }
}