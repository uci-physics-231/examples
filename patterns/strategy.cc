// A sample implementation of the Strategy design pattern in C++
// Verify that it compiles using g++ -c strategy.cc

#include <vector>

class AbsInterpolator {
public:
	virtual double interpolate(double x) const = 0;
};

class LinearInterpolator : public AbsInterpolator {
	LinearInterpolator(std::vector<double> const &xvec, std::std::vector<double> const &yvec);
	double interpolate(double x) const;
};

class SplineInterpolator : public AbsInterpolator {
	SplineInterpolator(std::vector<double> const &xvec, std::std::vector<double> const &yvec);
	double interpolate(double x) const;
};

//AbsInterpolator *interpolator1 = new LinearInterpolator(...);
//AbsInterpolator *interpolator2 = new SplineInterpolator(...);