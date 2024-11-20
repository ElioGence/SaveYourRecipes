import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { Recipe } from '../models/recipe';

@Injectable({
  providedIn: 'root',
})
export class RecipesService {
  private apiUrl = 'http://localhost:5000'; // Replace with your API URL
  private selectedRecipe = new BehaviorSubject<Recipe | null>(null);

  constructor(private http: HttpClient) {}

  getRecipes(user_id: string): Observable<Recipe[]> {
    return this.http.get<Recipe[]>(`${this.apiUrl}/recipes`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_id }  // Send user_id as a query parameter
    });
  }

  addRecipe(newRecipe: Recipe, user_id: string): Observable<Recipe> {
    return this.http.post<Recipe>(`${this.apiUrl}/recipes`, { ...newRecipe, user_id });
  }

  getSelectedRecipe(): Observable<Recipe | null> {
    return this.selectedRecipe.asObservable();
  }

  setSelectedRecipe(recipe: Recipe): void {
    this.selectedRecipe.next(recipe); // Update the selected recipe
  }
}
