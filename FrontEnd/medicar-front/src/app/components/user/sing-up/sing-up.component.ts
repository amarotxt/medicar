import { Component, OnInit, } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ToastrService } from 'ngx-toastr'
import { UserService } from '../shared/user.service';
import { User } from '../shared/user.model';

@Component({
  selector: 'app-sing-up',
  templateUrl: './sing-up.component.html',
  styleUrls: ['./sing-up.component.css']
})
export class SingUpComponent implements OnInit{
  user: User;
  emailPattern = "^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$";
  showPassWord : boolean = false;
  showConfirmPassWord : boolean = false;
  constructor(private userService: UserService, private toastr: ToastrService) { }

  ngOnInit() {
    this.resetForm();
  }

  resetForm(form?: NgForm) {
    if (form != null)
      form.reset();
    this.user = {
      UserName: '',
      Password: '',
      ConfirmPassword: '',
      Email: '',  
    }
  }

  OnSubmit(form: NgForm) {
    this.userService.registerUser(form.value)
      .subscribe((data: any) => {
        this.resetForm(form);
        this.toastr.success(`Usuário ${data['username']} Criado com sucesso`);
      } , error => {
        this.toastr.error(error) 
        console.error(error);
      });
  }

  ConfirmPassword = (ConfirmPassword,Password) => {
    if (ConfirmPassword  != Password) 
      return true
    else 
      return false

  } 

}
