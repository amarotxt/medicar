import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from './../user/shared/user.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  constructor(private router: Router, public userService: UserService) { }

  ngOnInit() {

  }

  openEspecialidade = () => {
    this.router.navigate(['list-especialidades']);
  }

}