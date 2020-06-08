import { ApiService } from './../../services/api.service';
import { Router, ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-agenda',
  templateUrl: './agenda.component.html',
  styleUrls: ['./agenda.component.css']
})
export class AgendaComponent implements OnInit {
  agendas: Array<any>;
  selctAgenda: any;
  constructor(
    // private router: Router, 
    private _route: ActivatedRoute,
    private api: ApiService
  ) { }
  ngOnInit(): void {
    const medicoId = +this._route.snapshot.params.medicoId;
    this.getAgendasMedico(medicoId);
    this.selctAgenda = null;
  }

  getAgendasMedico = (medicoId: number) => {
    this.api.getAgendasMedico(medicoId).subscribe(
      data => {
        this.agendas = data;
      }, error => {
        console.error(error);
      }
    );
  }

  selectHoraConsulta(hora: string){
    let consulta = {
      agenda: this.selctAgenda.id,
      horario: hora,
    }
    if(confirm(`Marcar consulta para o dia ${this.selctAgenda.dia} as ${hora}`)){
      this.api.postCreateConsulta(consulta).subscribe(
        data => {
          this.agendas = data;
        }, error => {
          console.error(error);
        }
      );
    }
  }

}
