import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../shared/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  userData = { username: '', password: '' };

  constructor(private authService: AuthService, private router: Router) { }

  login(userData: any) {
    this.authService.login(userData.username, userData.password).subscribe(response => {
      // Check if login was successful
      if (response.message === "Login successful") {
        // Store the user ID in localStorage
        localStorage.setItem('user_id', response.user_id.toString());

        // Redirect to the recipes page
        this.router.navigate(['/recipes']);
      } else {
        // Handle login failure (optional)
        alert('Login failed: ' + response.message);
      }
    }, error => {
      // Handle error response
      alert('Login failed: ' + (error.error?.message || 'Unknown error'));
    });
  }
}
