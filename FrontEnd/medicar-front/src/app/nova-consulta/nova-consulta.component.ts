import { Router } from '@angular/router';
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
  consulta : FormGroup;
  especialidadeSelect: boolean;
  // especialidades : FormGroup;
  // medicos : FormGroup;
  // datas : FormGroup;
  // horas : FormGroup;
  constructor( private api: ApiService,
              private router: Router, 
              private formBuild : FormBuilder) { 
     
  }

  ngOnInit(): void {
    this.especialidadeSelect = true;
    this.consulta = this.formBuild.group({
      especialidade: [null],
      medico : [null],
      data : [null], 
      hora : [null]
    })
    this.getEspecialidades();  
    this.consulta.get("especialidade").valueChanges.subscribe(data =>{
      console.log("especialidade",data)
      this.consulta.get("medico").setValue(null) ;
      this.getMedico(data)
    });
    this.consulta.get("medico").valueChanges.subscribe(data =>{
      if (!!data){
        this.getDataMedico(data)
      }      
    });
    this.consulta.get("data").valueChanges.subscribe(data =>{
      if (!!data){
        this.getHorarioMedico(data)
      }      
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
     
      this.api.getMedicosEspecialidade(especidalidade).subscribe(
        data => {
          this.medicosList = data;
        }, error => {
          console.error(error);
        }
      );
    }
  }

  getDataMedico = (medico) => {  
    if (!!medico){
      
      this.api.getAgendasMedico(medico).subscribe(
        data => {
          console.log("data ",data )
          if (data != null){
            if (data == []){
              this.dataList = ["Nao ha consultas para este medico"];
            }
            this.dataList = data;
            
          }else{
            this.dataList = ["Nao ha consultas para este medico"];
          }

        }, error => {
          console.error(error);
        }
      );
    }else{
      this.dataList = null;
      // console.log(this.dataList)
    }
  }

  getHorarioMedico = (data) => {
    console.log("horario",data)
    if (!!data){
      this.horasList = data["horarios"];      
    }else{
      this.horasList = ["Nenhum horario encontrado"];
    }

  }
  marcaConsulta = () => {
    let consulta = {
      agenda: this.consulta.value.data.id,
      horario: this.consulta.value.hora,
    }
    this.api.postCreateConsulta(consulta).subscribe(
      data => {
        this.router.navigate(['list-consultas']);
      }, error => {
        this.resetForm();
        console.error(error);
      }
    );
  }

  resetForm = () =>{
    this.consulta.reset()
  }
}
