import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../shared/services/auth.service';  // Path to your auth service
import { Router } from '@angular/router';  // Used to redirect after successful signup
import { ReactiveFormsModule } from '@angular/forms';  

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css'],
})

export class SignupComponent {
  signupForm: FormGroup;
  errorMessage: string = '';

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    // Initialize the signup form with validators
    this.signupForm = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(3)]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['', [Validators.required]],
    });
  }

  // Getter for easy access to form fields
  get f() {
    return this.signupForm.controls;
  }

  // Method to handle form submission
  onSubmit(): void {
    if (this.signupForm.invalid) {
      return;
    }

    const { username, email, password, confirmPassword } = this.signupForm.value;

    if (password !== confirmPassword) {
      this.errorMessage = 'Passwords do not match!';
      return;
    }

    this.authService.signup(username, password).subscribe(
      (response) => {
        // Handle successful signup (e.g., redirect to login or home)
        console.log('Signup successful:', response);
        this.router.navigate(['/login']);
      },
      (error) => {
        // Handle error
        this.errorMessage = error.error.message || 'Signup failed';
      }
    );
  }
}
