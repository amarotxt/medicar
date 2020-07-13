import { ApiService } from './../services/api.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-nova-consulta',
  templateUrl: './nova-consulta.component.html',
  styleUrls: ['./nova-consulta.component.css']
})
export class NovaConsultaComponent implements OnInit {
  especialidadesList : Array<any>;
  medicosList : Array<any>;
  dataList: Array<any>;
  horasList: Array<any>;
  especialidades : FormGroup;
  medicos : FormGroup;
  datas : FormGroup;
  horas : FormGroup;
  constructor( private api: ApiService, private formBuild : FormBuilder) { 
     
  }

  ngOnInit(): void {
    this.especialidades = this.formBuild.group({
      especialidade:[null],
    });
    this.getEspecialidades();
    this.medicos = this.formBuild.group({
      medico:[null],
    });
    this.datas = this.formBuild.group({
      data:[null],
    });
    this.horas = this.formBuild.group({
      hora:[null],
    });
  }

  getEspecialidades = () => {
    this.api.getAllEspecialidades().subscribe(
      data => {
        this.especialidadesList = data;
      }, error => {
        console.error(error);
      }
    );
  }
 
  getMedico = (especidalidade) => {
    if (especidalidade != null){
      console.log("especialidade",especidalidade)
      this.api.getMedicosEspecialidade(especidalidade["id"]).subscribe(
        data => {
          this.medicosList = data;
        }, error => {
          console.error(error);
        }
      );
    }
  }

  getDataMedico = (medico) => {
    if (medico != null){
      this.api.getAgendasMedico(medico["id"]).subscribe(
        data => {
          this.dataList = data;
          console.log("dataList ",this.dataList )
        }, error => {
          console.error(error);
        }
      );
    }
  }

  getHorarioMedico = (data) => {
    if (data != null){
      this.horasList = data["horarios"];
      
    }
  }
  
}
