import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from './../user/shared/user.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  userClaims: any;

  constructor(private router: Router, private userService: UserService) { }

  ngOnInit() {
    this.userService.getUserData().subscribe((data: any) => {
      this.userClaims = data;

    });
  }

  Logout() {
    localStorage.removeItem('userToken');
    this.router.navigate(['/login']);
  }
  openEspecialidade = () => {
    this.router.navigate(['list-especialidades']);
  }

}