import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
// import { Response } from "@angular/http";
import { Observable } from 'rxjs';
// import 'rxjs/add/operator/map';
import { User } from './user.model';
import { environment } from '../../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  readonly rootUrl =  environment.URLAPI;
  constructor(private http: HttpClient) { }

  registerUser(user: User) {
    const body: User = {
      username: user.username,
      password: user.password,
      email: user.email,
      firstname: user.firstname,
      lastname: user.lastname
    }
    var reqHeader = new HttpHeaders({'No-Auth':'True'});
    return this.http.post(`${this.rootUrl}usuario/`, body,{headers : reqHeader});
  }

  userAuthentication(userName, password) {
    var data = {'username':`${userName}` , 'password':`${password}`};
    var reqHeader = new HttpHeaders ({'Content-Type':'application/json','No-Auth':'True' });
    //({ 'Content-Type': 'application/x-www-urlencoded','No-Auth':'True' });
    return this.http.post(`${this.rootUrl}api-token-auth/`, data, { headers: reqHeader });
  }

  getUserData(){
   return  this.http.get(this.rootUrl+'usuario');
  }

}