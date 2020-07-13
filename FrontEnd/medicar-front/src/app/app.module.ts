import { ApiService } from './services/api.service';
import { RouterModule } from '@angular/router';
import { HttpClient, HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MatSliderModule } from '@angular/material/slider';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MedicosComponent } from './components/medicos/medicos.component';
import { EspecialidadesComponent } from './components/especialidades/especialidades.component';
import { AgendaComponent } from './components/agenda/agenda.component';
import { UserComponent } from './components/user/user.component';
import { LoginComponent } from './components/user/login/login.component';
import { HomeComponent } from './components/home/home.component';
import { SingUpComponent } from './components/user/sing-up/sing-up.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { UserService } from './components/user/shared/user.service';
import { AuthGuard } from './components/auth/auth.guard';
import { AuthInterceptor } from './components/auth/auth.interceptor';
import { ToastrModule } from 'ngx-toastr';
import { ConsultasComponent } from './consultas/consultas.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NovaConsultaComponent } from './nova-consulta/nova-consulta.component';

@NgModule({
  declarations: [
    AppComponent,
    MedicosComponent,
    EspecialidadesComponent,
    AgendaComponent,
    UserComponent,
    LoginComponent,
    SingUpComponent,
    HomeComponent,
    ConsultasComponent,
    NovaConsultaComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ToastrModule.forRoot(),
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatSliderModule,
  ],
  providers: [UserService,AuthGuard,ApiService,
    {
      provide : HTTP_INTERCEPTORS,
      useClass : AuthInterceptor,
      multi : true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
