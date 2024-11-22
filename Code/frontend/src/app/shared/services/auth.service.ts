import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, { username, password });
  }

  signUp(username: string, password: string, c_password:string): Observable<any> {
    if (password==c_password)
      return this.http.post(`${this.apiUrl}/signup`, { username, password });
    else
      return new Observable(observer => {
        observer.error({ message: 'Passwords do not match!' });
        observer.complete();
      });
  }

  
}
