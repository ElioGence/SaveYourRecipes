import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { Recipe } from '../shared/models/recipe';
import { RecipesService } from '../shared/services/recipes.service';
import { AppModule } from '../app.module';

@Component({
  selector: 'app-container',
  templateUrl: './container.component.html',
  styleUrls: ['./container.component.css'],
  providers: [RecipesService]
})

/**
 * NE PREND PAS EN COMPTE LES INGREDIENTS POUR LE MOMENT
 */
export class ContainerComponent implements OnInit {
  recipes : Recipe[] = [];
  selectedRecipe: Recipe = new Recipe ("Empty","","");
  addRecipeMode: boolean = false; // Nouvelle variable pour indiquer si le mode d'ajout de recette est activé
  selectMode : boolean = false;
  newRecipe: Recipe = new Recipe ("","",""); // Nouvelle recette en cours d'ajout

  constructor(private recipesService: RecipesService) {}

  ngOnInit() {
    this.recipes = this.recipesService.getRecipes();

    // Souscrire aux changements de la recette sélectionnée
    this.recipesService.getSelectedRecipe().subscribe((recipe: Recipe) => {
      this.selectedRecipe = recipe;
    });
  }

  onRecipeSelected(recipe: Recipe) {
    // Mettre à jour la recette sélectionnée via le service
    this.recipesService.setSelectedRecipe(recipe);
    this.selectMode=true;
  }

  onAddRecipe() {
    // Activer le mode d'ajout de recette
    this.addRecipeMode = true;
    // Réinitialiser la nouvelle recette
    this.newRecipe = { name: '', description: '', link: '' };
   }

  onSubmit() {
    // Ajouter la nouvelle recette à la liste 
    this.recipes.push(this.newRecipe);
    // Réinitialiser le mode d'ajout de recette
    this.addRecipeMode = false;
  }

  cancelCreation() {
    // Réinitialiser le mode d'ajout de recette à false
    this.addRecipeMode = false;
  }
}
