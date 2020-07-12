import { UserService } from './../components/user/shared/user.service';
import { Component, OnInit } from '@angular/core';
import { ApiService } from './../services/api.service';
import { tap } from 'rxjs/operators'
@Component({
  selector: 'app-consultas',
  templateUrl: './consultas.component.html',
  styleUrls: ['./consultas.component.css']
})
export class ConsultasComponent implements OnInit {
  consultas : any;
  public userData = {};

  constructor( private api: ApiService , private userService: UserService) { 
    console.log("aq",userService.usuario)
  }

  ngOnInit(): void {
    
    this.api.getConsultas().subscribe(
      data => {
        this.consultas = data;
        
      }, error => {
        console.error(error);
      }
    );
    // console.log("init",this.userService.usuario)
    this.userService.getUserData().subscribe(
        data => {
          this.userData = data
          
        }, error => {
          console.error(error);
        }
      ); ;
    console.log("init",this.userService.usuario)
    
  }
  Logout(){
    this.userService.Logout()
  }

  usuarioGetName(){
    if (this.userData == {}){
      return ""
    }
    else{
      return this.userData["username"]
    }
  }

}
