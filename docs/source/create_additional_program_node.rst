Create Additional Program Node
==========================================

This article explains step-by-step procedure to create/verify a program node in your existing URCap project in PolyScope X.

.. note::
   **Completion date:** 2025-April-15 · 
   **Last Updated:** 2026-05-18 (SDK 0.20.37)

**The environment prerequisite:**

- PolyScope X SDK **0.20.37**
- URSim **10.13**
- Angular **21**, ``@universal-robots/contribution-api`` **21.3.131**

.. tip::

   .. raw:: html

      <p>Reference sample project: <a href="https://github.com/FuNingHu/vision-template-x" target="_blank">https://github.com/FuNingHu/vision-template-x</a></p>

This is a typical program folder structure in a URCap project, and I want to add an additional program node
into project, let's name it "activate-camera-program".

----

Step 1: Create node files
--------------------------

Create node files under ``vision-template-x-frontend/src/app/components``.

It would be easier to duplicate an existing node together with its sub 6 files into a new folder under the same
directory of components, and rename all their name to "activate-camera-program-xxxx".

----

Step 2: Update activate-camera-program.node.ts
-----------------------------------------------

.. code-block:: typescript

   import { ProgramNode } from '@universal-robots/contribution-api';

   export interface ActivateCameraProgramNode extends ProgramNode {
       type: string;
       parameters?: {
           [key: string]: unknown;
       };
       lockChildren?: boolean;
       allowsChildren?: boolean;
   }

----

Step 3: Update activate-camera-program.component.ts
----------------------------------------------------

Update corresponding names of import component/templateUrl/styleUrls/class/Input, as below.

.. tip::
   **Angular 21 note:** ``standalone: false`` is required in the ``@Component({ ... })`` decorator, otherwise
   the new Angular CLI treats the component as standalone and ``NgModule.declarations`` registration breaks.

.. code-block:: typescript

   import { ChangeDetectionStrategy, ChangeDetectorRef, Component, Input, OnChanges, SimpleChanges } from '@angular/core';
   import { TranslateService } from '@ngx-translate/core';
   import { ProgramPresenter, ProgramPresenterAPI, RobotSettings } from '@universal-robots/contribution-api';
   import { ActivateCameraProgramNode } from './activate-camera-program.node';
   import { first } from 'rxjs/operators';

   @Component({
       templateUrl: './activate-camera-program.component.html',
       styleUrls: ['./activate-camera-program.component.scss'],
       changeDetection: ChangeDetectionStrategy.OnPush,
       standalone: false
   })

   export class ActivateCameraComponent implements OnChanges, ProgramPresenter {
       @Input() presenterAPI: ProgramPresenterAPI;
       @Input() robotSettings: RobotSettings;
       @Input() contributedNode: ActivateCameraProgramNode;

       constructor(
           protected readonly translateService: TranslateService,
           protected readonly cd: ChangeDetectorRef
       ) { }

       ngOnChanges(changes: SimpleChanges): void {
           // ... language change handling logic ...
       }

       async saveNode() {
           this.cd.detectChanges();
           await this.presenterAPI.programNodeService.updateNode(this.contributedNode);
       }
   }

----

Step 4: Revise activate-camera-program.component.spec.ts
---------------------------------------------------------

.. code-block:: typescript

   import {ComponentFixture, TestBed} from '@angular/core/testing';
   import {ActivateCameraComponent} from "./activate-camera-program.component";
   import {TranslateLoader, TranslateModule} from "@ngx-translate/core";
   import {Observable, of} from "rxjs";

   describe('ActivateCameraComponent', () => {
     let fixture: ComponentFixture<ActivateCameraComponent>;
     let component: ActivateCameraComponent;

     beforeEach(() => {
       TestBed.configureTestingModule({
         declarations: [ActivateCameraComponent],
         // ... TranslateModule imports ...
       }).compileComponents();

       fixture = TestBed.createComponent(ActivateCameraComponent);
       component = fixture.componentInstance;
     });

     // ... test cases ...
   });

----

Step 5: Update activate-camera-program.component.html
------------------------------------------------------

Update the display label. You can revise it later for a proper design.

.. code-block:: text

   <div *ngIf="contributedNode" class="inline-component">
       <p>Activate camera Prog. node works!!!</p>
   </div>

----

Step 6: Update activate-camera-program.behavior.worker.ts
----------------------------------------------------------

.. code-block:: typescript

   /// <reference lib="webworker" />
   import { ... } from '@universal-robots/contribution-api';
   import { ActivateCameraProgramNode } from './activate-camera-program.node';

   const createProgramNodeLabel = (node: ActivateCameraProgramNode): OptionalPromise<string> => 'Activate Program';

   const createProgramNode = (): OptionalPromise<ActivateCameraProgramNode> => ({
       type: 'funh-vision-template-x-activate-camera-program',
       // ⚠ This type will be used in many places, and should always be consistent.
       version: '1.0.0',
       lockChildren: false,
       allowsChildren: false,
       parameters: {},
   });

   // ... optional handlers: generateCodeBeforeChildren, generateCodeAfterChildren,
   //     generateCodePreamble, validator, allowsChild, allowedInContext, upgradeNode ...

   const behaviors: ProgramBehaviors = {
       programNodeLabel: createProgramNodeLabel,
       factory: createProgramNode,
       // ... register all handlers ...
   };

   registerProgramBehavior(behaviors);

----

Step 7: Copy the type string to i18n
--------------------------------------

Copy the type string from Step 6's ``createProgramNode`` method and paste it in
``vision-template-x-frontend/src/assets/i18n/en.json``, as below:

.. code-block:: json

   {
     "program": {
       "tree": {
         "nodes": {
           "...": "...",
           "funh-vision-template-x-activate-camera-program": "Activate Camera"
         }
       }
     }
   }

----

Step 8: Declaration in app.module.ts
-------------------------------------

Located at ``vision-template-x-frontend/src/app/app.module.ts``. There are 3 major sections that need
to add info:

- ``declarations``
- ``ngDoBootstrap``
- ``registerWorkersWithWebPack``

.. tip::
   **Angular 21 note:** ``new Worker(new URL(..., import.meta.url))`` requires ``module: "esnext"``
   (or ``"preserve"``) **plus** ``moduleResolution: "bundler"`` in ``tsconfig.json``. With the older
   default ``module: "es2022"`` + ``moduleResolution: "node"`` the build will fail with
   *"import.meta is only allowed when --module is ..."*.

.. code-block:: typescript

   import { DoBootstrap, Injector, NgModule } from '@angular/core';
   // ... other imports ...
   import { ActivateCameraComponent } from './components/activate-camera-program/activate-camera-program.component';

   @NgModule({
       declarations: [
           // ... other components ...
           ActivateCameraComponent,       // ← declare your component here
       ],
       imports: [ ... ],
       providers: [],
   })
   export class AppModule implements DoBootstrap {
       constructor(private injector: Injector) { }

       ngDoBootstrap() {
           // ... other customElements ...
           const activatecameraprogramComponent = createCustomElement(ActivateCameraComponent, { injector: this.injector });
           customElements.define('funh-vision-template-x-activate-camera-program', activatecameraprogramComponent);
       }

       registerWorkersWithWebPack() {
           // ... other workers ...
           new Worker(new URL('./components/activate-camera-program/activate-camera-program.behavior.worker.ts',
               import.meta.url), { name: 'activate-camera', type: 'module' });
       }
   }

----

Step 9: Add entry in contribution.json
----------------------------------------

Located at ``vision-template-x-frontend/src/contribution.json``. Here again, the **type value**
specified in Step 6 is used.

.. code-block:: text

   {
     "programNodes": [
       {
         "excludeFromToolbox": false,
         "translationPath": "assets/i18n/",
         "iconURI": "assets/icons/arrow-fat-right.svg",
         "behaviorURI": "activate-camera-program.worker.js",
         "presenterURI": "main.js",
         "componentTagName": "funh-vision-template-x-activate-camera-program"
       }
     ],
     ...
   }

.. note::
   Setting ``excludeFromToolbox`` to ``false`` means it will show up in the Toolbox in the Program page.
   Otherwise it will only be possible to insert through other nodes.

----

Step 10: Recompile project
---------------------------

Run from the **project root** (``vision-template-x/``), not the frontend folder — the orchestrator
``package.json`` delegates to the frontend automatically:

.. code-block:: bash

   npm run build
   npm run install-urcap -- --port 45000

Then refresh PolyScope to check whether the new node appears in the Program tree.
