import { Component } from '@angular/core';
import { AuthService } from '../../shared/services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {

  userData = { username: '', password: '', c_password: '' };

  constructor(private authService: AuthService, private router: Router) { }

  signUp(userData: any) {
    this.authService.signUp(userData.username, userData.password).subscribe(response => {
      if (response.message === "Signup successful") {
        // Redirect to login page after successful signup
        this.router.navigate(['/recipes']);
      }
    }, error => {
      alert(error.error.message);
    });
  }
}
