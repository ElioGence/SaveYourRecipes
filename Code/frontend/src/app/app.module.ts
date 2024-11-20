import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms'; 
import { FormsModule } from '@angular/forms'; 
import { CommonModule } from '@angular/common';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app.routes';
import { SignupComponent } from './components/signup/signup.component';  
import { AuthService } from './shared/services/auth.service';
import { RecipesComponent } from './components/recipes/recipes.component';
import { LoginComponent } from './components/login/login.component';
import { HeaderComponent } from './header/header.component';
import { ContainerComponent } from './container/container.component';
import { RecipeListComponent } from './recipe-list/recipe-list.component';
import { RecipeDetailsComponent } from './recipes-details/recipe-details.component';
import { SelectedDirective } from './shared/directives/selected.directive';
import { UserService } from './shared/services/user.service';
import { HttpClientModule } from '@angular/common/http'; 

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    HeaderComponent,
    ContainerComponent,
    RecipeListComponent,
    RecipeDetailsComponent,
    SelectedDirective,
    LoginComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    CommonModule,
    HttpClientModule,
  ],
  bootstrap: [AppComponent],
  providers: [UserService]
})
export class AppModule {}
