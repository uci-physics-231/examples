// Duck typing example in C++
// Compile and test with:
// gcc duck.cc
// .a/out

#include <cmath>
#include <iostream>

template <typename P>
double getMass(P const &p) {
	return std::sqrt(p.getEnergy()*p.getEnergy() - p.getMomentum()*p.getMomentum());
}

class Electron {
public:
	Electron(double p) : _p(p), _m(0.511) {
		_E = std::sqrt(p*p + _m*_m);
	}
	double getEnergy() const { return _E; }
	double getMomentum() const { return _p; }
private:
	double _m,_E,_p;
};

class SpaceShuttle {
public:
	SpaceShuttle(double fuel) : _fuel(fuel), _p(10), _m(10000) {
		_E = std::sqrt(_p*_p + _m*_m);
	}
	double getEnergy() const { return _E; }
	double getMomentum() const { return _p; }
	double getFuel() const { return _fuel; }
private:
	double _m,_E,_p,_fuel;
};

main() {
	Electron electron(1);
	std::cout << "Electron mass is " << getMass(electron) << std::endl;
	SpaceShuttle shuttle(1);
	std::cout << "Electron mass is " << getMass(shuttle) << std::endl;
}
