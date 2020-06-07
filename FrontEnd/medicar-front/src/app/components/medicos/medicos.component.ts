import { ApiService } from './../../services/api.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-medicos',
  templateUrl: './medicos.component.html',
  styleUrls: ['./medicos.component.css']
})
export class MedicosComponent implements OnInit {
  medicos: Array<any>;
  constructor(
    private router: Router, 
    private _route: ActivatedRoute,
    private api: ApiService
  ) { } 

  ngOnInit(): void {
    const especidalidadeId = +this._route.snapshot.params.especialidadeId;
    this.getMedicosEspecialicade(especidalidadeId);
  }

  getMedicosEspecialicade = (especidalidadeId: number) => {
    this.api.getMedicosEspecialidade(especidalidadeId).subscribe(
      data => {
        this.medicos = data;
      }, error => {
        console.error(error);
      }
    );
  }
  chosenMedico = (medicoId) =>  {
    console.log(medicoId);
    this.router.navigate(['list-agendas', medicoId]);
  }
}
