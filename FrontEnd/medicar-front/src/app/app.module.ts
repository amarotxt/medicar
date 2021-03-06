import { ApiService } from './services/api.service';
import { RouterModule } from '@angular/router';
import { HttpClient, HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MatSliderModule } from '@angular/material/slider';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserComponent } from './components/user/user.component';
import { LoginComponent } from './components/user/login/login.component';
import { SingUpComponent } from './components/user/sing-up/sing-up.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { UserService } from './components/user/shared/user.service';
import { AuthGuard } from './components/auth/auth.guard';
import { AuthInterceptor } from './components/auth/auth.interceptor';
import { ToastrModule } from 'ngx-toastr';
import { ConsultasComponent } from './consultas/consultas.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NovaConsultaComponent } from './nova-consulta/nova-consulta.component';
import { CookieService } from 'ngx-cookie-service';

@NgModule({
  declarations: [
    AppComponent,
    UserComponent,
    LoginComponent,
    SingUpComponent,
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
  providers: [UserService,AuthGuard,ApiService, CookieService,
    {
      provide : HTTP_INTERCEPTORS,
      useClass : AuthInterceptor,
      multi : true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
