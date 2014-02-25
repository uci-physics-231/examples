// A sample implementation of the FactoryMethod design pattern in C++
// Verify that it compiles using g++ -c factory.cc

#include <string>
#include <stdexcept>

class Particle {
public:
	static Particle *create(std::string const &name);
	double getMass() const { return _mass; }
protected:
	Particle(double mass) : _mass(mass) { }
private:
	double _mass;
};

class Electron : public Particle {
public:
	Electron() : Particle(0.511) { }
};

class Proton : public Particle {
public:
	Proton() : Particle(938.) { }
};

Particle *Particle::create(std::string const &name) {
	if(name == "electron") return new Electron();
	if(name == "proton") return new Proton();
	throw std::runtime_error("Unknown particle name: " + name);
}
