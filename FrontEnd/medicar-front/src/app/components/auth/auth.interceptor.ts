import { HttpInterceptor, HttpRequest, HttpHandler, HttpUserEvent, HttpEvent } from "@angular/common/http";
import { tap } from 'rxjs/operators';
import { Observable, pipe} from "rxjs";
import { Injectable } from "@angular/core";
import { Router } from "@angular/router";

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

    constructor(private router: Router) { }

    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        if (req.headers.get('No-Auth') == "True")
            return next.handle(req.clone());

        if (localStorage.getItem('userToken') != null) {
            console.log(localStorage.getItem('userToken'));
            const clonedreq = req.clone({
                headers: req.headers.set("Authorization", `Token ${localStorage.getItem('userToken')}`)
            });
            return next.handle(clonedreq).pipe(
                tap(
                succ => { },
                err => {
                    if (err.status === 401)
                        this.router.navigateByUrl('/login');
                }
                )
            )
        }
        else {
            this.router.navigateByUrl('/login');
        }
    }
}