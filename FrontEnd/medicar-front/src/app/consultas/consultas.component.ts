import { UserService } from './../components/user/shared/user.service';
import { Component, OnInit } from '@angular/core';
import { ApiService } from './../services/api.service';

@Component({
  selector: 'app-consultas',
  templateUrl: './consultas.component.html',
  styleUrls: ['./consultas.component.css']
})
export class ConsultasComponent implements OnInit {
  consultas : any;
  userClaims: any;

  constructor( private api: ApiService , private userService: UserService) { 
    
  }

  ngOnInit(): void {
    

     this.api.getConsultas().subscribe(
      data => {
        this.consultas = data;
      }, error => {
        console.error(error);
      }
    );
    // this.userService.getUserData().subscribe((data: any) => {
    //   this.userClaims = data;

    //     console.log(this.userClaims)
    // });
    
  }

}
