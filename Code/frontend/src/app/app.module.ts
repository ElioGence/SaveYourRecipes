import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms'; 
import { FormsModule } from '@angular/forms'; 

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app.routes';
import { SignupComponent } from './components/signup/signup.component';  
import { ApiService } from './shared/services/api.service';
import { AuthService } from './shared/services/auth.service';
import { RecipesComponent } from './components/recipes/recipes.component';
import { LoginComponent } from './components/login/login.component';
import { HeaderComponent } from './header/header.component';

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    LoginComponent,
    RecipesComponent,
    HeaderComponent,
    ApiService,
    AuthService
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    AppRoutingModule,
    FormsModule  
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
