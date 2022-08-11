import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { UploadDocumentComponent } from './upload-document/upload-document.component';
import { ViewDocumentComponent } from './view-document/view-document.component';

const routes: Routes = [
  {
    path:'view-document',
    component: ViewDocumentComponent
  },
  {
    path:'upload-document',
    component:UploadDocumentComponent
  },
  {
    path:'**',
    component:LandingPageComponent
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
