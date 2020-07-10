import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { ApiService } from './../../services/api.service';

@Component({
  selector: 'app-especialidades',
  templateUrl: './especialidades.component.html',
  styleUrls: ['./especialidades.component.css']
})
export class EspecialidadesComponent implements OnInit {
  especialidades: Array<any>;

  constructor(private api: ApiService, private router : Router) { 
  }

  ngOnInit(): void {
    this.getEspecialidades()
  }
  
  getEspecialidades = () => {
    this.api.getAllEspecialidades().subscribe(
      data => {
        this.especialidades = data;
      }, error => {
        console.error(error);
      }
    );
  }

  chosenEspecialidade = (especialidade) =>{
    this.router.navigate(['list-medicos', especialidade.id]);
  }
}
