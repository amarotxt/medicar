import { NovaConsultaComponent } from './nova-consulta/nova-consulta.component';
import { AgendaComponent } from './components/agenda/agenda.component';
import { MedicosComponent } from './components/medicos/medicos.component';
import { EspecialidadesComponent } from './components/especialidades/especialidades.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { UserComponent } from './components/user/user.component';
import { LoginComponent } from './components/user/login/login.component';
import { AuthGuard } from './components/auth/auth.guard';
import { SingUpComponent } from './components/user/sing-up/sing-up.component';
import { ConsultasComponent } from './consultas/consultas.component';


const routes: Routes = [
  { path: 'home', component: HomeComponent,canActivate:[AuthGuard] },
  {
    path: 'signup', component: UserComponent,
    children: [{ path: '', component: SingUpComponent }]
  },
  {
    path: 'login', component: UserComponent,
    children: [{ path: '', component: LoginComponent }]
  },
  { path : '', redirectTo:'/login', pathMatch : 'full'},
  {path: 'list-especialidades', component: EspecialidadesComponent},
  {path: 'list-consultas', component: ConsultasComponent},
  {path: 'consulta', component: NovaConsultaComponent},
  
  {path: 'list-medicos/:especialidadeId', component: MedicosComponent},
  {path: 'list-agendas/:medicoId', component: AgendaComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
