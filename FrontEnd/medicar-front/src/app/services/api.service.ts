import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from './../../environments/environment.prod';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class ApiService {
  baseUrl = environment.URLAPI;
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});
  constructor(private http: HttpClient) { }

  getAllEspecialidades(): Observable<any>{
    return this.http.get(`${this.baseUrl}especialidades/`,
    {headers: this.httpHeaders })
  }
  getMedicosEspecialidade(especialidadeId): Observable<any>{
    return this.http.get(`${this.baseUrl}medicos/?especialidade=${especialidadeId}`,
    {headers: this.httpHeaders });
  }
  getAgendasMedico(medicoId): Observable<any>{
    return this.http.get(`${this.baseUrl}agendas/?medico=${medicoId}`,
    {headers: this.httpHeaders });
  }
  postCreateConsulta(consulta: any): Observable<any>{
    return this.http.post(`${this.baseUrl}consultas/`, consulta,
    {headers: this.httpHeaders });
  }
}