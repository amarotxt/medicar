import { Component, OnInit } from '@angular/core';
import { HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';
import { UserService } from '../shared/user.service';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
  isLoginError : boolean = false;
  rememberMe : boolean =false
  public formData:any = {};
  constructor(private userService : UserService,
    private router : Router,
    private _cookie: CookieService) {
    if(!!_cookie.get('remember') && _cookie.get('remember') != "false"){   
        console.log("verificar",_cookie.get('remember'))
        this.formData["userName"] = _cookie.get('username')
        this.formData["password"] = _cookie.get('password')
    }        

  }

  ngOnInit() {

  }

  OnSubmit(userName,password, remember){
    if (remember){
      console.log("registerRemember")
      this._cookie.set('username',userName);
      this._cookie.set('password',password);
    }
    this._cookie.set('remember',remember);
    this.userService.userAuthentication(userName,password).subscribe(data => {
      localStorage.setItem('userToken',data["token"]);
      localStorage.setItem('userId',data["user_id"]);
      this.router.navigate(['/list-consultas']);
    }, error => {
      this.isLoginError = true;
      console.error(error);
      }
    );
    
  }
 
}




