import { Component, OnInit } from '@angular/core';
import { HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';
import { UserService } from '../shared/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
  isLoginError : boolean = false;
  constructor(private userService : UserService,private router : Router) { }

  ngOnInit() {
  }

  OnSubmit(userName,password){
    this.userService.userAuthentication(userName,password).subscribe(data => {
      
      console.log(this.userService.usuario)
      localStorage.setItem('userToken',data["token"]);
      localStorage.setItem('userId',data["user_id"]);
      this.router.navigate(['/list-consultas']);
    }, error => {
      console.error(error);
      }
    );
    
  }
}




