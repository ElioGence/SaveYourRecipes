import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RecipesComponent  } from './components/recipes/recipes.component';
import { LoginComponent  } from './components/login/login.component';
import { SignUpComponent  } from './components/signup/signup.component';
import { HeaderComponent } from './header/header.component';
import { RecipeListComponent } from './recipe-list/recipe-list.component';
import { RecipeDetailsComponent } from './recipes-details/recipe-details.component';
import { ContainerComponent } from './container/container.component';
import { AppComponent } from './app.component';

export const routes: Routes = [
    //{ path: '', component: AppComponent }, 
    { path: 'login', component: LoginComponent },        
    { path: 'sign-up', component: SignUpComponent },        
    { path: 'header', component: HeaderComponent }, 
    { path: 'container', component: ContainerComponent }, 
    { path: 'recipe-list', component: RecipeListComponent },  
    { path: 'recipe-details', component: RecipeDetailsComponent },  
    { path: 'app', component: AppComponent },  
    //{ path: '**', redirectTo: '/recipes' },               
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {}