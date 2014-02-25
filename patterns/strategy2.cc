// A sample implementation of the Strategy design pattern in C++
// using templates instead of inheritance, aka policy-based design.
// Verify that it compiles using g++ -c strategy2.cc

template <typename Algorithm>
class Interpolator : private Algorithm {
	using Algorithm::_interpolate;
public:
	double interpolate(double x) const {
		return _interpolate(x);
	}
};

class Linear {
protected:
	double _interpolate(double x);
};

class Spline {
protected:
	double _interpolate(double x);
};

// Interpolator<Linear> interpolator1(...);
// Interpolator<Spline> interpolator2(...);
