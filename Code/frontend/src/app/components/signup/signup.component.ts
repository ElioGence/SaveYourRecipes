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
    this.authService.signUp(userData.username, userData.password, userData.c_password).subscribe(response => {
      console.log(response)
      if (response.message === "Signup successful") {
        localStorage.setItem('user_id', response.user_id.toString());
        this.router.navigate(['/recipes']);
      }
    }, error => {
      alert(error.error.message);
    });
  }
}
