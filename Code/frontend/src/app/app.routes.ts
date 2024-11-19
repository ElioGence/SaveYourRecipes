import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RecipesComponent  } from './components/recipes/recipes.component';
import { LoginComponent  } from './components/login/login.component';
import { SignupComponent  } from './components/signup/signup.component';
import { HeaderComponent } from './header/header.component';
import { RecipeListComponent } from './recipe-list/recipe-list.component';
import { RecipeDetailsComponent } from './recipes-details/recipe-details.component';
import { ContainerComponent } from './container/container.component';

export const routes: Routes = [
    //{ path: '', redirectTo: '/recipes', pathMatch: 'full' }, // Default route redirects to Recipes
    //{ path: 'recipes', component: RecipesComponent },        // Recipes page
    //{ path: 'login', component: LoginComponent },            // Login page
    //{ path: 'signup', component: SignupComponent },          // Signup page
    { path: 'header', component: HeaderComponent },
    { path: 'recipe-list', component: RecipeListComponent },  
    { path: 'recipe-details', component: RecipeDetailsComponent },  
    { path: 'container', component: ContainerComponent },  
    //{ path: '**', redirectTo: '/recipes' },                  // Anything else redirects to Recipes
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {}