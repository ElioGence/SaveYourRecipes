import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RecipesComponent  } from './components/recipes/recipes.component';
import { LoginComponent  } from './components/login/login.component';
import { SignupComponent  } from './components/signup/signup.component';

export const routes: Routes = [
    { path: '', redirectTo: '/recipes', pathMatch: 'full' }, // Default route redirects to Recipes
    { path: 'recipes', component: RecipesComponent },        // Recipes page
    { path: 'login', component: LoginComponent },            // Login page
    { path: 'signup', component: SignupComponent },          // Signup page
    { path: '**', redirectTo: '/recipes' },                  // Anything else redirects to Recipes
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {}