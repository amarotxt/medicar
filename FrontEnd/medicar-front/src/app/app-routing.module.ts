import { AgendaComponent } from './components/agenda/agenda.component';
import { MedicosComponent } from './components/medicos/medicos.component';
import { EspecialidadesComponent } from './components/especialidades/especialidades.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


const routes: Routes = [
  {path: 'list-especialidades', component: EspecialidadesComponent},
  {path: 'list-medicos/:especialidadeId', component: MedicosComponent},
  {path: 'list-agendas/:medicoId', component: AgendaComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
