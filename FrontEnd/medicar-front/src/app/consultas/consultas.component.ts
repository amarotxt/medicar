import { Router } from '@angular/router';
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

  constructor( private api: ApiService , private userService: UserService, private router: Router) { 
  
  }

  ngOnInit(): void {
    this.getConsultas();
    // console.log("init",this.userService.usuario)
    this.userService.getUserData().subscribe(
        data => {
          this.userData = data
          
        }, error => {
          console.error(error);
        }
      ); 
    console.log("init",this.userService.usuario)
    
  }
  getConsultas(){
     
    this.api.getConsultas().subscribe(
      data => {
        this.consultas = data;
        
      }, error => {
        console.error(error);
      }
    );
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
  newColsulta(){
    this.router.navigate(['/consulta'])
  }

  deleteConsulta(consulta){
    this.api.deleteConsulta(consulta.id).subscribe(data =>{
      this.getConsultas();
    }, error =>{
      console.error(error);
    });
    
  }
}
