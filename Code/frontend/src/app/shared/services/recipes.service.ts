import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { Recipe } from '../models/recipe';

@Injectable({
  providedIn: 'root',
})
export class RecipesService {
  private apiUrl = 'http://localhost:5000'; 
  private selectedRecipe = new BehaviorSubject<Recipe | null>(null);

  constructor(private http: HttpClient) {}

  getRecipes(user_id: string): Observable<Recipe[]> {
    return this.http.get<Recipe[]>(`${this.apiUrl}/recipes`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_id }  
    });
  }

  addRecipe(newRecipe: Recipe, user_id: string): Observable<Recipe> {
    return this.http.post<Recipe>(`${this.apiUrl}/recipes`, { ...newRecipe, user_id });
  }

  deleteRecipe(recipeId: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/recipes/${recipeId}`);
  }
  
  modifyRecipe(recipeId: number, updatedRecipe: Recipe): Observable<Recipe> {
    return this.http.put<Recipe>(`${this.apiUrl}/recipes/${recipeId}`, updatedRecipe);
  }

  getSelectedRecipe(): Observable<Recipe | null> {
    return this.selectedRecipe.asObservable();
  }

  setSelectedRecipe(recipe: Recipe): void {
    this.selectedRecipe.next(recipe); 
  }
}
