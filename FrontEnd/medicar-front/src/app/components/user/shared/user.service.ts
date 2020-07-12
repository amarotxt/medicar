import { Router } from '@angular/router';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
// import { Response } from "@angular/http";
import { Observable } from 'rxjs';
// import 'rxjs/add/operator/map';
import { User } from './user.model';
import { environment } from '../../../../environments/environment';
import { tap } from 'rxjs/operators'
@Injectable({
  providedIn: 'root'
})
export class UserService {
  readonly rootUrl =  environment.URLAPI;
  usuario : any;
  constructor(private router: Router,  private http: HttpClient) { }

  registerUser(user: User) {
    const body = {
      username: user.UserName,
      password: user.Password,
      email: user.Email,
    }
    let reqHeader = new HttpHeaders({'No-Auth':'True'});
    return this.http.post(`${this.rootUrl}usuario/`, body,{headers : reqHeader});
  }

  userAuthentication(userName, password) {
    let data = {'username':`${userName}` , 'password':`${password}`};
    let reqHeader = new HttpHeaders ({'Content-Type':'application/json','No-Auth':'True' });
    //({ 'Content-Type': 'application/x-www-urlencoded','No-Auth':'True' });
  
   
    return this.http.post(`${this.rootUrl}api-token-auth/`, data, { headers: reqHeader });
  }

  getUserData(){
    this.usuario = localStorage.getItem('userId'); 
    return this.http.get(`${this.rootUrl}usuario/${this.usuario}`);
  }

  Logout() {
    localStorage.removeItem('userToken');
    localStorage.removeItem('userId');
    this.usuario = {};
    console.log("Logout")
    this.router.navigate(['/login']);
  }

}