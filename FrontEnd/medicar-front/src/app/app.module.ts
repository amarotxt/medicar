import { HttpClient, HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MedicosComponent } from './components/medicos/medicos.component';
import { EspecialidadesComponent } from './components/especialidades/especialidades.component';
import { AgendaComponent } from './components/agenda/agenda.component';

@NgModule({
  declarations: [
    AppComponent,
    MedicosComponent,
    EspecialidadesComponent,
    AgendaComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }
