import { NovaConsultaComponent } from './nova-consulta/nova-consulta.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { UserComponent } from './components/user/user.component';
import { LoginComponent } from './components/user/login/login.component';
import { AuthGuard } from './components/auth/auth.guard';
import { SingUpComponent } from './components/user/sing-up/sing-up.component';
import { ConsultasComponent } from './consultas/consultas.component';


const routes: Routes = [
  {
    path: 'signup', component: UserComponent,
    children: [{ path: '', component: SingUpComponent }]
  },
  {
    path: 'login', component: UserComponent,
    children: [{ path: '', component: LoginComponent }]
  },
  { path : '', redirectTo:'/login', pathMatch : 'full'},
  {path: 'list-consultas', component: ConsultasComponent},
  {path: 'consulta', component: NovaConsultaComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
