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
  constructor(
    private router: Router, 
    private _route: ActivatedRoute,
    private api: ApiService
  ) { }
  
  ngOnInit(): void {
    const medicoId = +this._route.snapshot.params.medicoId;
    this.getAgendasMedico(medicoId);
  }

  getAgendasMedico = (medicoId: number) => {
    console.log(medicoId)
    this.api.getAgendasMedico(medicoId).subscribe(
      data => {
        this.agendas = data;
      }, error => {
        console.error(error);
      }
    );
  }
}
