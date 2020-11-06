
SetFactory("OpenCASCADE");

//Merge "poreSpaceFull_sS100_10ks.brep";
//Merge "poreSpaceFull_sS1000_6ks.brep";
Merge "poreSpaceFull_sS500_4ks.brep";


X = .8;        // size of domain in x-direction
Y = .8;        // size of domain in y-direction
Z = 1.6;        // size of domain in z-direction

LC = .01/2.5;    // mesh critical length

all_surfaces[]=Surface "*";
dr = 1e-5;

back[] = Surface In BoundingBox {-dr,-dr,-dr,2*dr,Y+2*dr,Z+2*dr};
left[] = Surface In BoundingBox {-dr,-dr,-dr,X+2*dr,2*dr,Z+2*dr};
bottom[] = Surface In BoundingBox {-dr,-dr,-dr,X+2*dr,Y+2*dr,2*dr};

front[] = Surface In BoundingBox {X-dr,-dr,-dr,X+2*dr,Y+2*dr,Z+2*dr};
right[] = Surface In BoundingBox {-dr,Y-dr,-dr,X+2*dr,Y+2*dr,Z+2*dr};
top[] = Surface In BoundingBox {-dr,-dr,Z-dr,X+2*dr,Y+2*dr,Z+2*dr};

interior[]=all_surfaces[];
interior[]-=back[];
interior[]-=left[];
interior[]-=bottom[];
interior[]-=front[];
interior[]-=right[];
interior[]-=top[];

Physical Volume("Medium")={1};

Physical Surface("Back") = back[];
Physical Surface("Left") = left[];
Physical Surface("Bottom") = bottom[];
Physical Surface("Front") = front[];
Physical Surface("Right") = right[];
Physical Surface("Top") = top[];

Physical Surface("Interior") = interior[];


//Printf("allSurfaces = ",all_surfaces[]);
Printf("BackIndex = ",back[]);
Printf("LeftIndex = ",left[]);
Printf("BottomIndex = ",bottom[]);
Printf("FrontIndex = ",front[]);
Printf("RightIndex = ",right[]);
Printf("TopIndex = ",top[]);


// Define the meshing parameters
Field[1] = Box;
Field[1].VIn = LC;
Field[1].VOut = LC;
Field[1].XMin = 0;
Field[1].XMax = X;
Field[1].YMin = 0;
Field[1].YMax = Y;
Field[1].ZMin = 0;
Field[1].ZMax = Z;

Background Field = 1;

Mesh 3;